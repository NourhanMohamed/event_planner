package com.example.eventplanner;

import java.util.List;

import android.app.Activity;
import com.example.eventplanner.database.Event;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ImageView;
import android.widget.ListView;
import android.widget.TextView;


public class CustomList extends ArrayAdapter<Event> {
// TODO add the default image	
private final Activity context;
//private final String[] web;
//private final Integer[] imageId;
private final List<Event> events;
//private List<String> numbers;
private final int imageId;

//public CustomList(Activity context,
//String[] web, Integer[] imageId) {
//super(context, R.layout.list_single, web);
//this.context = context;
//this.web = web;
//this.imageId = imageId;
//
//}

public CustomList(Activity context, List<Event> e, int image) {
super(context, R.layout.list_single, e);
this.context = context;
this.events = e;
this.imageId = image;
System.out.println("HElloooooo7");
}
		

@Override
//public View getView(int position, View view, ViewGroup parent) {
//Log.e("NOURHAAAAAAAAAAAAAAN", "WESEL");
//System.out.println("Hello444");
//LayoutInflater inflater = context.getLayoutInflater();
//View rowView= inflater.inflate(R.layout.list_single, null, true);
//TextView EventName = (TextView) rowView.findViewById(R.id.name);
//TextView EventDate = (TextView) rowView.findViewById(R.id.date);
//TextView EventDescription = (TextView) rowView.findViewById(R.id.description);
//ImageView imageView = (ImageView) rowView.findViewById(R.id.img);
//EventName.setText(events.get(position).getName());
//EventDate.setText((CharSequence) events.get(position).getEventDate());
//EventDescription.setText(events.get(position).getDescription());
//imageView.setImageResource(imageId);
//return rowView;
//}

public View getView(int position, View view, ViewGroup parent) {
System.out.println("EEEEEEEEEEEEEEEEEEEEH");
LayoutInflater inflater = context.getLayoutInflater();
View rowView= inflater.inflate(R.layout.list_single, null, true);
TextView txtTitle = (TextView) rowView.findViewById(R.id.name);

ImageView imageView = (ImageView) rowView.findViewById(R.id.img);
txtTitle.setText("HELLO");

imageView.setImageResource(imageId);
return rowView;
}
}