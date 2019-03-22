<!DOCTYPE html>
<html lang="en">
<head>
    <title>Example of Adding Newlines in PHP</title>
</head>
<body>


<?php
echo nl2br("Hello World!I've made a \r\n change to this !!");

echo "Will this work properly ????";

echo "This line was added 27/02/2019 @ 16:49";


echo "If you view the source of output frame \r\n you will find a newline in this string.";
echo "<br>";
echo nl2br("You will find the \n newlines in this string \r\n on the browser window.");
?>

</body>
</html>   
