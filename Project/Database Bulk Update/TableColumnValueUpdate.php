<?php

	// Your MySQL connection configuration
	$servername = "localhost";
	$username   = "root";
	$password   = "";
	$dbname     = "property";

	// Create connection
	$conn = new mysqli($servername, $username, $password, $dbname);

	// Check connection
	if ($conn->connect_error) {
		die("Connection failed: " . $conn->connect_error);
	}

	// Select posts from wp_posts table where post_type is 'Property'
	$sql_select_posts = "SELECT ID FROM wp_posts WHERE post_type = 'Property'";
	$result_posts     = $conn->query($sql_select_posts);

	if ($result_posts->num_rows > 0) {
		// Counter for serializing property_id
		$counter = 1;

		// Loop through each post
		while($row_posts = $result_posts->fetch_assoc()) {
			$post_id = $row_posts['ID'];
			
			// Serialize property_id
			$new_property_id = 'TP_' . sprintf('%06d', $counter);
			
			// Select * from wp_postmeta table where post_id is $post_id and meta_key is '_property_property_id'
			$sql_select_metas = "SELECT * FROM wp_postmeta WHERE post_id = $post_id AND meta_key = '_property_property_id'";
			$result_metas = $conn->query($sql_select_metas);
			if ($result_metas->num_rows > 0) {
				// Updated the unique meta_value into wp_postmeta table
				$sql_update_postmeta = "UPDATE wp_postmeta SET meta_value='$new_property_id' WHERE post_id = $post_id AND meta_key = '_property_property_id'";
				if ($conn->query($sql_update_postmeta) === TRUE) {
					echo "Record updated successfully";
				} else {
					echo "Error updating record: " . $conn->error;
				}
			} else {
				// Insert the unique meta_value into wp_postmeta table
				$sql_insert_postmeta = "INSERT INTO wp_postmeta (post_id, meta_key, meta_value) VALUES ($post_id, '_property_property_id', '$new_property_id')";
				if ($conn->query($sql_insert_postmeta) === TRUE) {
					echo "New record inserted successfully";
				} else {
					echo "Error inserting record: " . $conn->error;
				}
			}           
			
			// Increment the counter for the next iteration
			$counter++;
		}
	} else {
		echo "0 results found in wp_posts table";
	}

	// Close MySQL connection
	$conn->close();

?>
