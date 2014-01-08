package com.example.eventplanner;

import java.util.ArrayList;
import java.util.List;

import android.app.Activity;
import android.content.ClipData.Item;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Toast;

import com.example.eventplanner.database.EventsDataSource;
import com.example.eventplanner.database.Statics;
import com.example.eventplanner.database.UsersDataSource;
import com.example.eventplanner.database.Event;

public class HomeActivity extends Activity {
	private EventsDataSource datasource;
	ListView list;
	List<String> myList = new ArrayList<String>();
	String[] web = { "Google Plus", "Twitter", "Windows", "Bing", "Itunes",
			"Wordpress", "Drupal" };
	Integer[] imageId = { R.drawable.image1, R.drawable.image2,
			R.drawable.image3, R.drawable.image4, R.drawable.image5,
			R.drawable.image6, R.drawable.image7

	};

	@Override
	// protected void onCreate(Bundle savedInstanceState) {
	// super.onCreate(savedInstanceState);
	// setContentView(R.layout.activity_home);
	//
	//
	// CustomList adapter = new
	// CustomList(HomeActivity.this, web, imageId);
	// list=(ListView)findViewById(R.id.list);
	// list.setAdapter(adapter);
	// list.setOnItemClickListener(new AdapterView.OnItemClickListener() {
	//
	// @Override
	// public void onItemClick(AdapterView<?> parent, View view,
	// int position, long id) {
	// Toast.makeText(HomeActivity.this, "To delete " +web[+ position]
	// +" keep clicking on it" , Toast.LENGTH_SHORT).show();
	//
	// }
	// });
	// list.setOnItemLongClickListener(new AdapterView.OnItemLongClickListener()
	// {
	//
	// public boolean onItemLongClick(AdapterView<?> parent,
	// View view, int position, long id) {
	// Toast.makeText(HomeActivity.this, "You will delete " +web[+ position],
	// Toast.LENGTH_SHORT).show();
	// return false;
	// }
	// });
	//
	//
	//
	//
	// }
	public void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_home);

		datasource = new EventsDataSource(this);
		datasource.open();

		list = (ListView) findViewById(R.id.list);
		System.out.println(Statics.username);
		List<Event> values = datasource.getAllItems(Statics.username);
		System.out.println("Helloooo1");
		System.out.println(values.toString());
		// CustomList adapter = new
		// CustomList(HomeActivity.this, values, R.drawable.image2);
		myList.add("ONE");
		myList.add("TWO");
		myList.add("Three");
		CustomList adapter = new CustomList(HomeActivity.this, values,
				R.drawable.image2);
		System.out.println("Helloooo5");
		// ArrayAdapter<Item> adapter = new ArrayAdapter<Item>(this,
		// android.R.layout.simple_list_item_1);
		System.out.println(list.toString());
		list.setAdapter(adapter);
	
		list.setOnItemLongClickListener(new AdapterView.OnItemLongClickListener() {

			public boolean onItemLongClick(AdapterView<?> parent, View view,
					int position, long id) {
				Toast.makeText(HomeActivity.this,
						"You will delete " + web[+position], Toast.LENGTH_SHORT)
						.show();
				return false;
			}
		});
		System.out.println("Helloooo6");
		Log.w("NOOOO", "GAAAAT");
		datasource.close();
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
		case R.id.signout: {
			UsersDataSource uds = new UsersDataSource(getApplicationContext());
			uds.open();
			uds.updateSignOut();
			uds.close();
			Intent i = new Intent(HomeActivity.this, LoginActivity.class);
			finish();
			startActivity(i);
			return true;
		}
		case R.id.newevent: {
			Intent i = new Intent(HomeActivity.this, NewEventActivity.class);
			startActivity(i);
			return true;
		}
		}

		return super.onMenuItemSelected(featureId, item);
	}
}
