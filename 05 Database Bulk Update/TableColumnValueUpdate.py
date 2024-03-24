import mysql.connector

# Your MySQL connection configuration
config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'property',
    'raise_on_warnings': True
}

# Create connection
conn = mysql.connector.connect(**config)

# Check connection
if conn.is_connected():
    print('Connected to MySQL database')

    # Select posts from wp_posts table where post_type is 'Property'
    cursor = conn.cursor()
    sql_select_posts = "SELECT ID FROM wp_posts WHERE post_type = 'Property'"
    cursor.execute(sql_select_posts)
    posts = cursor.fetchall()

    if posts:
        # Counter for serializing property_id
        counter = 1

        # Loop through each post
        for post in posts:
            post_id = post[0]

            # Serialize property_id
            new_property_id = 'TP_{:06d}'.format(counter)

            # Select from wp_postmeta table where post_id is $post_id and meta_key is '_property_property_id'
            sql_select_meta = "SELECT * FROM wp_postmeta WHERE post_id = %s AND meta_key = '_property_property_id'"
            cursor.execute(sql_select_meta, (post_id,))
            meta_result = cursor.fetchall()

            if meta_result:
                # Update the unique meta_value into wp_postmeta table
                sql_update_meta = "UPDATE wp_postmeta SET meta_value=%s WHERE post_id = %s AND meta_key = '_property_property_id'"
                cursor.execute(sql_update_meta, (new_property_id, post_id))
                conn.commit()
                print("Record updated successfully")
            else:
                # Insert the unique meta_value into wp_postmeta table
                sql_insert_meta = "INSERT INTO wp_postmeta (post_id, meta_key, meta_value) VALUES (%s, '_property_property_id', %s)"
                cursor.execute(sql_insert_meta, (post_id, new_property_id))
                conn.commit()
                print("New record inserted successfully")

            # Increment the counter for the next iteration
            counter += 1

    else:
        print("0 results found in wp_posts table")

    # Close cursor and connection
    cursor.close()
    conn.close()
    print('MySQL connection closed')
else:
    print('Connection to MySQL database failed')
