<?php include("a_config.php");?>
<!DOCTYPE HTML>
<html>
<head>
	<?php include("head-tag-contents.php");?>
</head>
<body>

<?php include("design-top.php");?>
<?php include("navigation.php");?>

<div class="container" id="main-content">
    <h2>Hasil Ekstraksi</h2>
    <p>Ekstraksi berita dilakukan dengan mencari angka terdekat dari keyword yang anda masukkan dan waktu yang tersedia pada kalimat yang dipilih. Tetap berpikir positif untuk Indonesia yang lebih baik. Hasil ini tidak mempengaruhi masa depan anda! Jangan lupa untuk berdoa dan berbuat baik ya!</p>
    <div class="title" id="bagianIsi">
    <?php
        $keyword = "$_POST[keyword]";
        $algoritma = "<b>$_POST[algoritma]</b>";
        echo "Keyword: $keyword";
        echo "<br> Algoritma yang anda pilih: $algoritma <br>";
        echo "<h5> Hasil Ekstraksi Berita</h5>";
        $countfiles = count($_FILES['file']['name']);
        if(isset($_POST['submit'])){
            // Looping all files
            for($i=0; $i< $countfiles; $i++){
                $filename = $_FILES['file']['name'][$i];
                
                move_uploaded_file($_FILES['file']['tmp_name'][$i],'..\\test\\'.$filename);
                //algoritmanya disini brow
                if ($algoritma == "<b>KMP</b>"){
                    echo "<br> File ke-$i : $filename <br>";
                    echo shell_exec("python kmp.py $filename $keyword");
                } elseif ($algoritma == "<b>BM</b>") {
                    echo "<br> File ke-$i : $filename <br>";
                    echo shell_exec("python bm.py $filename $keyword");
                } elseif ($algoritma == "<b>Regex</b>"){
                    echo " <br> File ke-$i : $filename <br>";
                    echo shell_exec("python rgx.py $filename $keyword");
                } else{
                    echo "<br> Algoritma belum dipilih!<br> ";
                }
                echo "<br>";
                // move_uploaded_file($_FILES['file']['tmp_name'][$i],'upload/'.$filename);
            }
        }
    ?>
    <br>
    <br>
</div>

<?php include("footer.php");?>

</body>
</html>