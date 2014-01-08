package com.example.eventplanner.database;

import java.sql.Timestamp;

public class Event {
	private long id;
	private String name;
	private String description;
	private String username;
	private Timestamp event_date;
	private String uri;

	public String getDescription() {
		return description;
	}

	public void setDescription(String description) {
		this.description = description;
	}

	public String getUserName() {
		return username;
	}

	public void setUserName(String username) {
		this.username = username;
	}

	public Timestamp getEventDate() {
		return event_date;
	}

	public void setEventDate(Timestamp event_date) {
		this.event_date = event_date;
	}

	public long getId() {
		return id;
	}

	public void setId(long id) {
		this.id = id;
	}

	public String getName() {
		return name;
	}

	public void setName(String eventName) {
		this.name = eventName;
	}

	@Override
	public String toString() {
		return name;
	}

	public String getUri() {
		return uri;
	}

	public void setUri(String uri) {
		this.uri = uri;
	}
}
