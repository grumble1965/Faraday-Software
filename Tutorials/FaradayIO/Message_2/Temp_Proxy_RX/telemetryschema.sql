create table telemetry (
    keyid  integer primary key autoincrement not null,
	'faradayport' integer default null,
	'packettype' integer default null,
	'aprf' integer default null,
	'apcallsign' character(9) default null,
	'apid' integer default null,
	callsign character(9) default null,
	id integer default null,
	rtcsec integer default null,
	rtcmin integer default null,
	rtchour integer default null,
	rtcday integer default null,
	rtcdow integer default null,
	rtcmon integer default null,
	rtcyear integer default null,
	'apgpsfix' integer default null,
	'aplatdeg' integer default null,
	'aplatdec' real default null,
	'aplatdir' character(1) default null,
	'aplondeg' integer default null,
	'aplondec' real default null,
	'aplondir' character(1) default null,
	'apaltitude' integer default null,
	'apaltunits' character(1) default null,
	'apspeed' real default null,
	'aphdop' real default null,
	gpsfix integer default null,
	latdeg integer default null,
	latdec real default null,
	latdir character(1) default null,
	londeg integer default null,
	londec real default null,
	londir character(1) default null,
	altitude integer default null,
	altunits character(1) default null,
	speed real default null,
	hdop real default null,
	'gpio0' integer default null,
	'gpio1' integer default null,
	'gpio2' integer default null,
	adc0 integer default null,
	adc1 integer default null,
	adc2 integer default null,
	adc3 integer default null,
	adc4 integer default null,
	adc5 integer default null,
	adc6 integer default null,
	adc7 integer default null,
	adc8 integer default null,
	'apepoch' integer default null,
	destcallsign character(9) default null,
	destid integer default null,
	crc integer default null,
	uChar_auto_cutdown_timer_state_status integer default null,
	uChar_cutdown_event_state_status integer default null,
	uInt_timer_set integer default null,
	uInt_timer_current integer default null
);

create table scaledtelemetry (
	keyid integer primary key autoincrement not null,
	callsign character(9) default null,
	id integer default null,
	epoch integer default null,
	adc0scaled real default null,
	adc1scaled real default null,
	adc2scaled real default null,
	adc3scaled real default null,
	adc4scaled real default null,
	adc5scaled real default null,
	adc6scaled real default null,
	adc7scaled real default null,
	adc8scaled real default null,
	paenable integer default null,
	lnaenable integer default null,
	hgmselect integer default null,
	mosfet integer default null,
	led1 integer default null,
	led2 integer default null,
	gpsreset integer default null,
	gpsstandby integer default null,
	button integer default null,
	gpio0 integer default null,
	gpio1 integer default null,
	gpio2 integer default null,
	gpio3 integer default null,
	gpio4 integer default null,
	gpio5 integer default null,
	gpio6 integer default null,
	gpio7 integer default null,
	gpio8 integer default null,
	gpio9 integer default null
);

create table faradayio (
	keyid integer primary key autoincrement not null,
	keyname character (25) default null,
	callsign character(9) default null,
	id integer default null,
	adc0m real default 0.00058838,
	adc0b real default 0,
	adc1m real default 0.00058838,
	adc1b real default 0,
	adc2m real default 0.00058838,
	adc2b real default 0,
	adc3m real default 0.00058838,
	adc3b real default 0,
	adc4m real default 0.00058838,
	adc4b real default 0,
	adc5m real default 0.00058838,
	adc5b real default 0,
	adc6m real default 0.006472,
	adc6b real default 0,
	adc7m real default 0.2615,
	adc7b real default -305.778,
	adc8m real default 0.00117676,
	adc8b real default 0,
	tempcal real default -28.168
);


create table HABApplication (
    keyid  integer primary key autoincrement not null,
	'status_bitmask' integer default null,
	'uInt_timer_set' integer default null,
	'uInt_timer_remaining' integer default null
);

create table faradayDebug (
	keyid integer primary key autoincrement not null,
	callsign character(9) default null,
	id integer default null,
	epoch integer default null,
	faradayport integer default null,
	packettype integer default null,
	aprf integer default null,
	bootcount integer default null,
	resetcount integer default null,
	bor integer default null,
	rstnmi integer default null,
	svsl integer default null,
	svsh integer default null,
	svmlovp integer default null,
	svmhovp integer default null,
	wdtto integer default null,
	flashkeyviolation integer default null,
	fllunlock integer default null,
	peripheralconfigcnt integer default null,
	accessviolation integer default null
);

create table faradaySystemSettings (
	keyid integer primary key autoincrement not null,
	callsign character(9) default null,
	id integer default null,
	epoch integer default null,
	faradayport integer default null,
	packettype integer default null,
	aprf integer default null,
	rffreq0 integer default null,
	rffreq1 integer default null,
	rffreq2 integer default null,
	rfpwr integer default null
);