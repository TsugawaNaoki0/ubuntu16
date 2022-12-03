<?php

$zip = new ZipArchive();

if ($zip->open('./login_database.zip') === true) {
	if ($zip->extractTo('./') === true) {
		$zip->close();
	} else {
		exit('Extract Error');
	}
} else {
	exit('Open Error 1');
}


if ($zip->open('./organized_homepage.zip') === true) {
	if ($zip->extractTo('./') === true) {
		$zip->close();
	} else {
		exit('Extract Error');
	}
} else {
	exit('Open Error 2');
}
echo 'Unzip Complete.';

echo shell_exec(" mv ./login_database/* ./ ");

echo 'login_database was opened.';

?>
