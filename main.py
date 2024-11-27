<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WhatsApp Automation</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 0;
            padding: 0;
            background-color: #f9f9f9;
        }
        .container {
            margin: 50px auto;
            padding: 20px;
            width: 300px;
            background: #fff;
            border: 1px solid #ddd;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            font-size: 20px;
            margin-bottom: 20px;
        }
        input, select, button {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>WhatsApp Automation</h1>
        <form>
            <input type="text" placeholder="Your Phone Number" name="phone_number" required>
            <label for="send-to">Send to:</label>
            <select id="send-to" name="send_to">
                <option value="target_numbers">Target Numbers</option>
            </select>
            <input type="text" placeholder="Targets (comma-separated)" name="targets" required>
            <input type="text" placeholder="Message File Path" name="message_file" required>
            <input type="text" placeholder="Hater Name" name="hater_name" required>
            <input type="number" placeholder="Delay (seconds)" name="delay" required>
            <button type="submit">Start Automation</button>
        </form>
    </div>
</body>
</html>
