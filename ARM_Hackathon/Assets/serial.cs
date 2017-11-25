using UnityEngine;
using System.Collections;
using System.IO.Ports;

public class serialRotation : MonoBehaviour {

	SerialPort stream = new SerialPort("/dev/tty.usbmodem1422", 9600); //Set the port (com4) and the baud rate (9600, is standard on most devices)

	void Start () {
		stream.Open(); //Open the Serial Stream.
	}

	// Update is called once per frame
	void Update () {
		string value = stream.ReadLine(); //Read the information
		Debug.Log(value);
	}
}
