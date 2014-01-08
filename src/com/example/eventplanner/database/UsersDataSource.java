package com.example.eventplanner.database;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.SQLException;
import android.database.sqlite.SQLiteDatabase;

public class UsersDataSource {

	// Database fields
	private SQLiteDatabase database;
	private SQLiteHelper dbHelper;

	public UsersDataSource(Context context) {
		dbHelper = new SQLiteHelper(context);
	}

	public void open() throws SQLException {
		database = dbHelper.getWritableDatabase();
	}

	public void close() {
		dbHelper.close();
	}

	public User createUser(String username, String password) {
		ContentValues values = new ContentValues();
		values.put("username", username);
		values.put("password", password);
		long insertId = database.insert("users", null, values);
		Cursor cursor = database.query("users", new String[] { "id",
				"username", "password" }, "id = " + insertId, null, null, null,
				null);
		cursor.moveToFirst();
		User newUser = cursorToUser(cursor);
		cursor.close();
		return newUser;
	}

	private User cursorToUser(Cursor cursor) {
		User user = new User();
		user.setId(cursor.getLong(0));
		user.setName(cursor.getString(1));
		user.setPassword(cursor.getString(2));
		return user;
	}

	public boolean checkUserRegistered(String username, String password) {
		Cursor cursor = database.query("users", new String[] { "username",
				"password" }, "username ='" + username + "' AND password='"
				+ password + "'", null, null, null, null);
		return cursor.moveToFirst();
	}

	public boolean checkUsernameExist(String username) {
		Cursor cursor = database.query("users", new String[] { "username" },
				"username ='" + username + "'", null, null, null, null);
		return cursor.moveToFirst();
	}

	public void updateSignIn(String username) {
		ContentValues values = new ContentValues();
		values.put("signed_in", 1);
		database.update("users", values, "username = '" + username + "'", null);
	}

	public void updateSignOut() {
		ContentValues values = new ContentValues();
		values.put("signed_in", 0);
		database.update("users", values, null, null);
	}

	public int autoSignIn() {
		Cursor cursor = database.query("users", new String[] { "id", "username" },
				"signed_in = 1", null, null, null, null);
		boolean empty = !cursor.moveToFirst();
		if (!empty) {
			Statics.username = cursor.getString(1);
			return cursor.getCount();
		}
		return -1;
	}
}