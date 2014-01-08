package com.example.eventplanner.database;

import java.sql.Timestamp;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.List;
import java.util.TimeZone;

import android.content.ContentResolver;
import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.SQLException;
import android.database.sqlite.SQLiteDatabase;
import android.net.Uri;
import android.provider.CalendarContract;
import android.util.Log;
import android.widget.Toast;

public class EventsDataSource {

	// Database fields
	private SQLiteDatabase database;
	private SQLiteHelper dbHelper;
	private Context context;

	public EventsDataSource(Context context) {
		this.context = context;
		dbHelper = new SQLiteHelper(context);
	}

	public void open() throws SQLException {
		database = dbHelper.getWritableDatabase();
	}

	public void close() {
		dbHelper.close();
	}

	public Event createEvent(String username, String name, String description,
			Timestamp datetime) {
		// ContentValues event = new ContentValues();
		// event.put("calendar_id", "2");
		// event.put("title", name);
		// event.put("description", description);
		// event.put("eventTimezone", TimeZone.getDefault().getID());
		// long startTime = datetime.getTime();
		// event.put("dtstart", startTime);
		// event.put("dtend", startTime+3600000);
		// event.put("allDay", 1);
		// Uri eventsUri = Uri.parse("content://com.android.calendar/events");
		// Uri uri = context.getContentResolver().insert(eventsUri, event);
		// Log.e("uri", uri.getPath());

		long startMillis = 0;
		long endMillis = 0;
		Calendar beginTime = Calendar.getInstance();
		beginTime.set(datetime.getDate(), datetime.getMonth(),
				datetime.getYear(), datetime.getHours(), datetime.getMinutes());
		startMillis = beginTime.getTimeInMillis();
		Calendar endTime = Calendar.getInstance();
		endTime.set(datetime.getDate(), datetime.getMonth(),
				datetime.getYear(), datetime.getHours() + 1, datetime.getMinutes());
		endMillis = endTime.getTimeInMillis();

		// Insert Event
		ContentResolver cr = context.getContentResolver();
		ContentValues values = new ContentValues();
		TimeZone timeZone = TimeZone.getDefault();
		values.put(CalendarContract.Events.DTSTART, startMillis);
		values.put(CalendarContract.Events.DTEND, endMillis);
		values.put(CalendarContract.Events.EVENT_TIMEZONE, timeZone.getID());
		values.put(CalendarContract.Events.TITLE, name);
		values.put(CalendarContract.Events.DESCRIPTION,
				description);
		values.put(CalendarContract.Events.CALENDAR_ID, 2);
		Uri uri = cr.insert(CalendarContract.Events.CONTENT_URI, values);
		Log.e("uri", uri.getPath());

		// Retrieve ID for new event
//		String eventID = uri.getLastPathSegment();

		ContentValues valuesDB = new ContentValues();
		valuesDB.put("name", name);
		valuesDB.put("description", description);
		valuesDB.put("event_date", datetime.toString());
		valuesDB.put("username", username);
		valuesDB.put("uri", uri.getPath());
		long insertId = -1;
		try {
			insertId = database.insert("events", null, valuesDB);
		} catch (android.database.sqlite.SQLiteConstraintException e) {
			toast("Event name already exists");
		}
		if (insertId == -1) {
			return null;
		}
		Cursor cursor = database.query("events", new String[] { "id", "name",
				"description", "event_date", "username", "uri" }, "id" + " = "
				+ insertId, null, null, null, null);
		cursor.moveToFirst();
		Event newEvent = cursorToEvent(cursor);
		cursor.close();
		return newEvent;
	}

	public void deleteEvent(String eventName) {
		database.delete("events", "name" + " = '" + eventName + "'", null);
	}

	public List<Event> getAllItems(String username) {
		List<Event> events = new ArrayList<Event>();

		Cursor cursor = database.query("events", new String[] { "id", "name",
				"description", "event_date", "username", "uri" },
				"username = '" + username + "'", null, null, null, null);
		System.out.println("Helloooo2");
		cursor.moveToFirst();
		System.out.println("Helloooo3");
		while (!cursor.isAfterLast()) {
			Event event = cursorToEvent(cursor);
			events.add(event);
			cursor.moveToNext();
		}
		// make sure to close the cursor
		cursor.close();
		return events;
	}

	private Event cursorToEvent(Cursor cursor) {
		Event event = new Event();
		event.setId(cursor.getLong(0));
		event.setName(cursor.getString(1));
		event.setDescription(cursor.getString(2));
		event.setEventDate(Timestamp.valueOf(cursor.getString(3)));
		event.setUserName(cursor.getString(4));
		event.setUri(cursor.getString(5));
		return event;
	}

	public void toast(String text) {
		Toast.makeText(context, text, Toast.LENGTH_SHORT).show();
	}
}