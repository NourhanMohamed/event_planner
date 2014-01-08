package com.example.eventplanner;

import java.sql.Timestamp;
import java.util.ArrayList;
import java.util.List;

import org.apache.http.protocol.HTTP;

import android.app.Activity;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.content.pm.ResolveInfo;
import android.os.Bundle;
import android.view.ContextMenu;
import android.view.ContextMenu.ContextMenuInfo;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.AdapterView;
import android.widget.Button;
import android.widget.ListView;
import android.widget.Toast;

import com.example.eventplanner.database.Event;
import com.example.eventplanner.database.EventsDataSource;
import com.example.eventplanner.database.Statics;
import com.example.eventplanner.database.UsersDataSource;

public class HomeActivity extends Activity implements OnClickListener {
	private EventsDataSource datasource;
	CustomList adapter;
	Button newEvent;
	ListView list;
	List<String> myList = new ArrayList<String>();
	String[] web = { "Google Plus", "Twitter", "Windows", "Bing", "Itunes",
			"Wordpress", "Drupal" };
	Integer[] imageId = { R.drawable.image1, R.drawable.image2,
			R.drawable.image3, R.drawable.image4, R.drawable.image5,
			R.drawable.image6, R.drawable.image7

	};

	@Override
	public void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_home);
		newEvent = (Button) findViewById(R.id.create_newevent);
		newEvent.setOnClickListener(this);

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
		adapter = new CustomList(HomeActivity.this, values, R.drawable.image2);
		System.out.println("Helloooo5");
		// ArrayAdapter<Item> adapter = new ArrayAdapter<Item>(this,
		// android.R.layout.simple_list_item_1);
		System.out.println(list.toString());
		list.setAdapter(adapter);
		registerForContextMenu(list);
		// list.setOnItemLongClickListener(new
		// AdapterView.OnItemLongClickListener() {
		//
		// public boolean onItemLongClick(AdapterView<?> parent, View view,
		// int position, long id) {
		//
		// Toast.makeText(HomeActivity.this,
		// "You will delete " + web[+position], Toast.LENGTH_SHORT)
		// .show();
		// return false;
		// }
		// });
		// System.out.println("Helloooo6");
		// Log.w("NOOOO", "GAAAAT");
		datasource.close();
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.home, menu);
		return true;
	}

	@Override
	public void onCreateContextMenu(ContextMenu menu, View v,
			ContextMenuInfo menuInfo) {
		AdapterView.AdapterContextMenuInfo info = (AdapterView.AdapterContextMenuInfo) menuInfo;
		menu.setHeaderTitle("Options");
		String[] menuItems = getResources().getStringArray(R.array.menu);
		for (int i = 0; i < menuItems.length; i++) {
			menu.add(Menu.NONE, i, i, menuItems[i]);
		}
	}

	@Override
	public boolean onContextItemSelected(MenuItem item) {
		AdapterView.AdapterContextMenuInfo info = (AdapterView.AdapterContextMenuInfo) item
				.getMenuInfo();
		EventsDataSource eds = new EventsDataSource(getApplicationContext());
		eds.open();
		List<Event> events = eds.getAllItems(Statics.username);

		String listItemName = events.get(info.position).getName();
		if (item.getTitle().equals("Delete")) {
			adapter.remove(adapter.getItem(info.position));
			adapter.notifyDataSetChanged();
			eds.deleteEvent(listItemName);
		} else if (item.getTitle().equals("Share")) {
			Event e = adapter.getItem(info.position);
			Intent emailIntent = new Intent(Intent.ACTION_SEND);

			emailIntent.setType(HTTP.PLAIN_TEXT_TYPE);
			emailIntent.putExtra(Intent.EXTRA_SUBJECT, "Event Invitation");
			Timestamp ts = e.getEventDate();
			String min = ts.getMinutes() == 0 ? "00" : ts.getMinutes() + "";
			emailIntent.putExtra(
					Intent.EXTRA_TEXT,
					"I am cordially inviting you to the event " + e.getName()
							+ "\nDescription: " + e.getDescription()
							+ "\nThe Event is held on " + ts.getDate() + "/"
							+ ts.getMonth() + "/" + ts.getYear() + " at "
							+ ts.getHours() + ":" + min);
			PackageManager packageManager = getPackageManager();
			List<ResolveInfo> activities = packageManager
					.queryIntentActivities(emailIntent, 0);
			boolean isIntentSafe = activities.size() > 0;
			if (isIntentSafe) {
				startActivity(emailIntent);
			}
		}

		eds.close();
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

	public void toast(String text) {
		Toast.makeText(getApplicationContext(), text, Toast.LENGTH_SHORT)
				.show();
	}

	@Override
	public void onClick(View v) {
		Intent i = new Intent(HomeActivity.this, NewEventActivity.class);
		startActivity(i);
	}
}
