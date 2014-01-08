package com.example.eventplanner;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.example.eventplanner.database.UsersDataSource;

public class SignUpActivity extends Activity {
	EditText username;
	EditText password;
	EditText confirmPassword;
	Button signUp;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_sign_up);
		
		username = (EditText) findViewById(R.id.name);
		password = (EditText) findViewById(R.id.pass);
		confirmPassword = (EditText) findViewById(R.id.confirm_pass);
		signUp = (Button) findViewById(R.id.sign_up);
		
		signUp.setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				String userName = username.getText().toString();
				String passwordText = password.getText().toString();
				String confirmText = confirmPassword.getText().toString();
				
				if(!passwordText.equals(confirmText))
					toast("Password mismatch");
				else
				{
					UsersDataSource uds = new UsersDataSource(getApplicationContext());
					uds.open();
					boolean userExists = uds.checkUsernameExist(userName);
					if(userExists)
						toast("Username exists!");
					else
					{
						uds.createUser(userName, passwordText);
						Intent i = new Intent(SignUpActivity.this, LoginActivity.class);
						finish();
						startActivity(i);
					}
					uds.close();
				}
			}
		});
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.sign_up, menu);
		return true;
	}
	
	public void toast(String text) {
		Toast.makeText(getApplicationContext(), text, Toast.LENGTH_SHORT)
				.show();
	}

}
