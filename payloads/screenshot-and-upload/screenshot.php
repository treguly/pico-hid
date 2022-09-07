<?php
$putdata = fopen("php://input", "r");
$fp = fopen("uploads/screenshot.bmp", "w");
while ($data = fread($putdata, 1024))
        fwrite($fp, $data);
fclose($fp);
fclose($putdata);
?>