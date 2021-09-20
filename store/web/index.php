<html>


<head><title>Fruit Shop</title></head>
<body>
	<h1>Welcome to the Fruit Shop</h1>
	<ul>
		<?php

		$json = file_get_contents('http://fruits-service/');
		$obj = json_decode($json);
		$fruits = $obj ->fruits;
		foreach( $fruits as $fruit){

			echo "<li>$fruit</li>";

		}


		?>
	</ul>
	</body>
</html>
