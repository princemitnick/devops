<?php
$servername = getenv('DB_HOST');
$username = getenv('DB_USER');
$password = getenv('DB_PASS');
$dbname = getenv('DB_NAME');

// Connexion MySQL
$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die("Connexion échouée: " . $conn->connect_error);
}

// Créer une table
$conn->query("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50))");

// Ajouter un utilisateur
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST["name"];
    $conn->query("INSERT INTO users (name) VALUES ('$name')");
}

// Afficher les utilisateurs
$result = $conn->query("SELECT * FROM users");
echo "<h2>Utilisateurs</h2><ul>";
while ($row = $result->fetch_assoc()) {
    echo "<li>" . $row["name"] . "</li>";
}
echo "</ul>";

?>

<form method="post">
    <input type="text" name="name" placeholder="Nom">
    <input type="submit" value="Ajouter">
</form>
