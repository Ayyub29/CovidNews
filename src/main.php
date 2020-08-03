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
    <form method='post' action='hasil.php' enctype='multipart/form-data'>
        <h2>Selamat Datang!</h2>
        <p>Ekstraksi berita dilakukan dengan mencari angka terdekat dari keyword yang anda masukkan dan waktu yang tersedia pada kalimat yang dipilih. Silakan menggunakan website untuk Indonesia yang lebih baik. Silahkan baca petunjuk penggunaan di Tab 'Petunjuk'. Jangan lupa untuk berdoa dan berbuat baik ya!</p>
        <div class="title" id="bagianIsi">
            <br>
            <h4 style="text-align:left" id= "cmdInputFile"><?php echo 'Masukkan Teks Berita'; ?></h3>
            <input type="file" name="file[]" id="file" multiple>
            <br>
            <br>
            <br>
            </div>
            <h4 style="text-align: left"><?php echo 'Pilih Algoritma'; ?></h3>
            <!--Opsi algoritma yang dapat digunakan-->
            <div class="radio-container">
                <input type="radio" id="KMP" name="algoritma" value="KMP">
                <label class ="radio" for="KMP">Knuth-Morris-Pratt</label><br>

                <input type="radio" id="Boyer-Moore" name="algoritma" value="BM">
                <label class ="radio" for="Boyer-Moore">Boyer-Moore</label><br>
    
                <input type="radio" id="Regex" name="algoritma" value="Regex">
                <label class ="radio" for="Regex">Regex</label><br>
            </div>
            <br>
            <h4 style="text-align: left">Masukkan Keyword</h3>
            <div class="search-bar">
                <input class="input-box" type = "text" placeholder="Masukan keyword" name="keyword" >
                <input type="submit" name="submit" value="submit">
            </div>
            <br>
            <br>
        </form>
</div>

<?php include("footer.php");?>

</body>
</html>