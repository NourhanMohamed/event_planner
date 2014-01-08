package com.example.eventplanner;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.AdapterView;
import android.widget.AdapterView.OnItemSelectedListener;
import android.widget.Spinner;

import com.example.eventplanner.database.UsersDataSource;

public class NewEventActivity extends Activity implements OnItemSelectedListener{
	Spinner spinnerDays;
	Spinner spinnerMonths;
	Spinner spinnerYears;
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_new_event);
		
		spinnerDays = (Spinner) findViewById(R.id.days);
		spinnerMonths = (Spinner) findViewById(R.id.months);
		spinnerYears = (Spinner) findViewById(R.id.years);
		spinnerDays.setOnItemSelectedListener(this);
		spinnerMonths.setOnItemSelectedListener(this);
		spinnerYears.setOnItemSelectedListener(this);
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
			Intent i = new Intent(NewEventActivity.this,
					LoginActivity.class);
			finish();
			startActivity(i);
			return true;
		}

		return super.onMenuItemSelected(featureId, item);
	}

	@Override
	public void onItemSelected(AdapterView<?> parent, View view, int pos,
			long id) {
		
		
	}

	@Override
	public void onNothingSelected(AdapterView<?> parent) {
		
		
	}

}
