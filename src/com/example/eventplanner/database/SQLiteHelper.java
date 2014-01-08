package com.example.eventplanner.database;

import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

public class SQLiteHelper extends SQLiteOpenHelper {
	public SQLiteHelper(Context context) {
		super(context, "events1.db", null, 1);
	}

	@Override
	public void onCreate(SQLiteDatabase db) {
		db.execSQL("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT,"
				+ "username varchar(40) UNIQUE NOT NULL,"
				+ "password varchar(40) NOT NULL,"
				+ "signed_in INTEGER DEFAULT 0);");
		db.execSQL("CREATE TABLE IF NOT EXISTS events (id INTEGER PRIMARY KEY AUTOINCREMENT,"
				+ "name varchar(40) UNIQUE NOT NULL,"
				+ "description varchar(200) NOT NULL,"
				+ "event_date DATETIME NOT NULL," 
				+ "uri varchar(100),"
				+ "username varchar(4), "
				+ "FOREIGN KEY (username) REFERENCES users(username) ON DELETE CASCADE ON UPDATE CASCADE);");
	}

	@Override
	public void onUpgrade(SQLiteDatabase arg0, int arg1, int arg2) {

	}
}
