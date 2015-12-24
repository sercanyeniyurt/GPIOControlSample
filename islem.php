<?php

# The role and status of sent Ajax number makes the work app.py send the file.

$islem = $_POST['islem'];
$role = $_POST['role'];

echo shell_exec("sudo python /var/www/html/app.py ".$role." ".$islem."");


?>
