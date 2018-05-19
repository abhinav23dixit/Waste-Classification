<?php

if(isset($_POST['submit'])) {
	$file = $_FILES['file'];

	$fileName = $_FILES['file']['name'];
	$fileTmpName = $_FILES['file']['tmp_name'];
	$fileSize = $_FILES['file']['size'];
	$fileError = $_FILES['file']['error'];
	$fileType = $_FILES['file']['type'];

	$fileExt = explode('.', $fileName);
	$fileActualExt = strtolower(end($fileExt));

	$allowed = array('jpg','jpeg','png');
	if (in_array($fileActualExt, $allowed)) {
		if($fileError === 0) {
			$fileNameNew = "file.jpg";
			$fileDestination = 'uploads/'.$fileNameNew;
			move_uploaded_file($fileTmpName, $fileDestination);
			header("Location: result.php");
		}else {
			echo "Error!";
		}
	}else {
		echo "Invalid image!";
	}
	
	$result = exec("C:\\Users\\John\\Anaconda3\\python.exe C:\\Users\\John\\Desktop\\PredScript.py");
	//$resultArray = json_decode($result);
	//foreach ($resultArray as $row) {
	//	echo $row . "<BR>";
	//}
}
?>