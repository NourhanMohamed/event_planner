package com.example.eventplanner.database;

import java.sql.Timestamp;
import java.util.ArrayList;
import java.util.List;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.SQLException;
import android.database.sqlite.SQLiteDatabase;

public class EventsDataSource {

	// Database fields
	private SQLiteDatabase database;
	private SQLiteHelper dbHelper;

	public EventsDataSource(Context context) {
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

		Cursor cursor = database.query("event", new String[] { "id", "name",
				"description", "event_date" }, "username = '" + username + "'",
				null, null, null, null);

		cursor.moveToFirst();
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