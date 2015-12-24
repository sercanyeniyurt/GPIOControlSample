<?php


$islem = $_POST['islem'];
$role = $_POST['role'];

echo shell_exec("sudo python /var/www/html/app.py ".$role." ".$islem."");


?>