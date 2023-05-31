<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Retrieve form data
    $name = $_POST['name'];
    $phone = $_POST['phone'];
    $email = $_POST['email'];
    $service = $_POST['service'];
    $location = $_POST['location'];
    $message = $_POST['message'];

    // Compose email message
    $to = 'kfaamardesubombhack@gmail.com';
    $subject = 'New Form Submission';
    $body = "
    Name: $name
    Phone: $phone
    Email: $email
    Service: $service
    Location: $location
    Message: $message
    ";
    $headers = "From: $email\r\n";
    
    // Send the email
    if (mail($to, $subject, $body, $headers)) {
        echo 'Email sent successfully!';
    } else {
        echo 'Error sending email.';
    }
}
?>