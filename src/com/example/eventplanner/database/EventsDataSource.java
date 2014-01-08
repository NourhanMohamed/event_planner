package com.example.eventplanner.database;

import java.sql.Timestamp;
import java.util.ArrayList;
import java.util.List;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.SQLException;
import android.database.sqlite.SQLiteDatabase;
import android.net.Uri;
import android.util.Log;

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
		ContentValues values = new ContentValues();
		values.put("name", name);
		values.put("description", description);
		values.put("event_date", datetime.toString());
		values.put("username", username);
		long insertId = database.insert("events", null, values);
		ContentValues event = new ContentValues();
		event.put("calendar_id", "nourhan.abdeltawab@gmail.com");
		event.put("title", name);
		event.put("description", description);
		long startTime = datetime.getTime();
		event.put("dtstart", startTime);
		event.put("allDay", 1);
		Uri eventsUri = Uri.parse("content://calendar/events");
		Uri url = context.getContentResolver().insert(eventsUri, event);
		Cursor cursor = database.query("events", new String[] { "id", "name",
				"description", "event_date", "username" }, "id" + " = "
						+ insertId, null, null, null, null);
		cursor.moveToFirst();
		Event newEvent = cursorToEvent(cursor);
		cursor.close();
		return newEvent;
	}

	public void deleteEvent(String eventName) {
		database.delete("events", "name" + " = " + eventName, null);
	}

	public List<Event> getAllItems(String username) {
		List<Event> events = new ArrayList<Event>();

		Cursor cursor = database.query("events", new String[] { "id", "name",
				"description", "event_date" }, "username = '" + username + "'",
				null, null, null, null);
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
		return event;
	}
}