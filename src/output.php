<?php
    
?>

<!DOCTYPE HTML>
<html>
    <head>
        <h1> COVID NEWS INFO EXTRACTOR </h1>
    </head>
    <body>
    <?php
        #Inisialisasi variabel
        $jumlah = 4;
        $namaFile = "<b>$_POST[fileToUpload]</b>";
        $keyword = "<b>$_POST[keyword]</b>";
        $algoritma = "<b>$_POST[algoritma]</b>";
        echo "<br>Nama Berita: $namaFile<br>";
        echo "<br>Keyword: $keyword<br>";
        echo "<br>Algoritma terpilih: $algoritma<br>";
        for($i = $jumlah; $i>0; $i--)
        {
            echo ($jumlah-$i+1) . ". Jumlah: Waktu: <br>";
        }

        echo "<br> <a href='pembuat.php'>Pembuat</a>";
    ?>
    </body>
</html>