package com.example.eventplanner;

import java.sql.Timestamp;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.AdapterView;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.TimePicker;
import android.widget.Toast;

import com.example.eventplanner.database.Event;
import com.example.eventplanner.database.EventsDataSource;
import com.example.eventplanner.database.Statics;
import com.example.eventplanner.database.UsersDataSource;

public class NewEventActivity extends Activity implements OnClickListener {
	EditText title;
	EditText description;
	Spinner spinnerDays;
	Spinner spinnerMonths;
	Spinner spinnerYears;
	TimePicker timePick;
	Button create;
	

	int day, month, year;
	int hours, mins;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_new_event);

		title = (EditText) findViewById(R.id.editText1);
		description = (EditText) findViewById(R.id.editText2);
		spinnerDays = (Spinner) findViewById(R.id.dayspinner);
		spinnerMonths = (Spinner) findViewById(R.id.monthspinner);
		spinnerYears = (Spinner) findViewById(R.id.yearspinner);
		timePick = (TimePicker) findViewById(R.id.timePicker1);
		spinnerDays
				.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {

					@Override
					public void onItemSelected(AdapterView<?> parent,
							View view, int position, long id) {
						day = Integer.parseInt(parent.getItemAtPosition(
								position).toString());
					}

					@Override
					public void onNothingSelected(AdapterView<?> arg0) {
						// TODO Auto-generated method stub

					}

				});
		spinnerMonths
				.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {

					@Override
					public void onItemSelected(AdapterView<?> parent,
							View view, int position, long id) {

						month = Integer.parseInt(parent.getItemAtPosition(
								position).toString());

					}

					@Override
					public void onNothingSelected(AdapterView<?> arg0) {
						// TODO Auto-generated method stub

					}

				});
		spinnerYears
				.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {

					@Override
					public void onItemSelected(AdapterView<?> parent,
							View view, int position, long id) {

						year = Integer.parseInt(parent.getItemAtPosition(
								position).toString());

					}

					@Override
					public void onNothingSelected(AdapterView<?> arg0) {
						// TODO Auto-generated method stub

					}

				});
		create = (Button) findViewById(R.id.create_event);
		create.setOnClickListener(this);
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.new_event, menu);
		return true;
	}

	@Override
	public boolean onMenuItemSelected(int featureId, MenuItem item) {
		switch (item.getItemId()) {
		case R.id.signout:
			UsersDataSource uds = new UsersDataSource(getApplicationContext());
			uds.open();
			uds.updateSignOut();
			uds.close();
			Intent i = new Intent(NewEventActivity.this, LoginActivity.class);
			finish();
			startActivity(i);
			return true;
		}

		return super.onMenuItemSelected(featureId, item);
	}

	@Override
	public void onClick(View v) {
		int id = v.getId();
		if(id == R.id.create_event){
			hours = timePick.getCurrentHour();
			mins = timePick.getCurrentMinute();
			Timestamp ts = new Timestamp(year, month, day, hours, mins, 0, 0);
			String name = title.getText().toString();
			String desc = description.getText().toString();
			if(name.isEmpty() || desc.isEmpty()){
				toast("Title and description can not be empty");
			} else {
				EventsDataSource eds = new EventsDataSource(getApplicationContext());
				eds.open();
				Event event = eds.createEvent(Statics.username, name, desc, ts);
				eds.close();
				
				if(event == null){
					toast("Could not create event");
				}
				
				Intent i = new Intent(NewEventActivity.this, HomeActivity.class);
				finish();
				startActivity(i);
			}
		}
	}

	public void toast(String text) {
		Toast.makeText(getApplicationContext(), text, Toast.LENGTH_SHORT)
				.show();
	}

}
