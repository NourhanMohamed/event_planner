package com.example.eventplanner;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;

import com.example.eventplanner.database.UsersDataSource;

public class HomeActivity extends Activity {

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_home);
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.home, menu);
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
			Intent i = new Intent(HomeActivity.this,
					LoginActivity.class);
			finish();
			startActivity(i);
			return true;
		}

		return super.onMenuItemSelected(featureId, item);
	}
}
