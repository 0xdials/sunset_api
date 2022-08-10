#!/bin/bash
# Uses API to return sunset/sunrise time to return proper "Morning" "Afternoon" and "Evening" tags.

lat=47.6062
long=-122.3321
current_time=`date +%H`


get_times() {
	request=`curl -ksf "https://api.sunrise-sunset.org/json?lat="$lat"&lng="$long"&formatted=0"`


	if [ ! -z "$request" ]; then
		sunrise_time=`echo "$request" | jq ".results.sunrise" | tr -d '"'`
		local_sunrise_time=`date +%H -d $sunrise_time`

		sunset_time=`echo "$request" | jq ".results.sunset" | tr -d '"'`
		local_sunset_time=`date +%H -d $sunset_time`
	
	fi
}


time_compare() {
	
	if [[ $current_time -ge $local_sunset_time ]]; then
		echo " Evening"

	elif [[ $current_time -ge $local_sunrise_time ]] && [[ $current_time -lt 12 ]]; then
		echo " Morning"
	
	elif [[ $current_time -ge 12 ]]; then
		echo " Afternoon"
	
	else
		echo " Evening"
	fi
			
}

get_times
time_compare
