package com.example.eventplanner;

import android.app.ActionBar;
import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.view.MotionEvent;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.Toast;

import com.example.eventplanner.database.Statics;
import com.example.eventplanner.database.UsersDataSource;
import com.example.eventplanner.util.SystemUiHider;

public class LoginActivity extends Activity implements OnClickListener {
	private static final boolean AUTO_HIDE = true;
	private static final int AUTO_HIDE_DELAY_MILLIS = 100;
	private static final int HIDER_FLAGS = SystemUiHider.FLAG_HIDE_NAVIGATION;
	private SystemUiHider mSystemUiHider;
	private EditText username;
	private EditText password;
	private CheckBox rememberMe;
	private Button sign_in;
	private Button sign_up;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		ActionBar actionBar = getActionBar();
		actionBar.hide();

		setContentView(R.layout.activity_login);

		final View contentView = findViewById(R.id.fullscreen_content);

		username = (EditText) findViewById(R.id.username);
		password = (EditText) findViewById(R.id.password);
		sign_in = (Button) findViewById(R.id.sign_in);
		sign_up = (Button) findViewById(R.id.create_account);
		rememberMe = (CheckBox) findViewById(R.id.remember_me);

		sign_in.setOnClickListener(this);
		sign_up.setOnClickListener(this);
		
		UsersDataSource uds = new UsersDataSource(getApplicationContext());
		uds.open();
		int user = uds.autoSignIn();
		if(user > 0){
			Intent i = new Intent(LoginActivity.this, HomeActivity.class);
			finish();
			startActivity(i);
		}
		uds.close();

		mSystemUiHider = SystemUiHider.getInstance(this, contentView,
				HIDER_FLAGS);
		mSystemUiHider.setup();
	}

	@Override
	protected void onPostCreate(Bundle savedInstanceState) {
		super.onPostCreate(savedInstanceState);
		delayedHide(100);
	}

	View.OnTouchListener mDelayHideTouchListener = new View.OnTouchListener() {
		@Override
		public boolean onTouch(View view, MotionEvent motionEvent) {
			if (AUTO_HIDE) {
				delayedHide(AUTO_HIDE_DELAY_MILLIS);
			}
			return false;
		}
	};

	Handler mHideHandler = new Handler();
	Runnable mHideRunnable = new Runnable() {
		@Override
		public void run() {
			mSystemUiHider.hide();
		}
	};

	/**
	 * Schedules a call to hide() in [delay] milliseconds, canceling any
	 * previously scheduled calls.
	 */
	private void delayedHide(int delayMillis) {
		mHideHandler.removeCallbacks(mHideRunnable);
		mHideHandler.postDelayed(mHideRunnable, delayMillis);
	}

	@Override
	public void onClick(View v) {
		int view = v.getId();
		Intent i = new Intent();
		switch (view) {
		case R.id.sign_in: {
			String userName = username.getText().toString();
			String passwordText = password.getText().toString();
			UsersDataSource uds = new UsersDataSource(getApplicationContext());
			uds.open();
			boolean verified = uds.checkUserRegistered(userName, passwordText); 
			if (verified) {
				Statics.username = userName;
				i = new Intent(LoginActivity.this, HomeActivity.class);
				if(rememberMe.isChecked())
					uds.updateSignIn(userName);
				finish();
				startActivity(i);
			}
			else
				toast("Incorrect credentials");
			uds.close();
			break;
		}
		case R.id.create_account: {
			i = new Intent(LoginActivity.this, SignUpActivity.class);
			startActivity(i);
			break;
		}
		}
	}

	public void toast(String text) {
		Toast.makeText(getApplicationContext(), text, Toast.LENGTH_SHORT)
				.show();
	}
}
