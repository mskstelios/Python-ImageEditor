
<body>

  <h1>Image Editor</h1>

  <p>This is a simple image editor application built using PyQt5 in Python. It allows users to open a folder, choose an image from the list, apply various filters, and save the edited image.</p>

  <h2>How to Use</h2>

  <h3>1. Open a Folder</h3>
  <ul>
        <li>Click on the "Open Folder" button to choose a directory containing images.</li>
        <li>The list on the left will display compatible image files in the selected folder.</li>
  </ul>

  <h3>2. Choose an Image</h3>
    <ul>
        <li>Select an image from the list to display it on the right side.</li>
    </ul>

  <h3>3. Apply Filters</h3>
    <ul>
        <li>Check the checkboxes to apply the corresponding filters:</li>
        <ul>
            <li>"Left" - Rotate the image 90 degrees to the left.</li>
            <li>"Mirror" - Flip the image horizontally.</li>
            <li>"Sharpness" - Enhance the sharpness of the image.</li>
            <li>"B&W" - Convert the image to black and white.</li>
            <li>"Blur" - Apply a box blur filter to the image.</li>
            <li>"Normal" - Reset the image to its original state.</li>
        </ul>
    </ul>

  <h3>4. Save Edited Image</h3>
    <ul>
        <li>Click the "Save Edited Image" button to save the edited image in a 'Modified' folder within the original folder.</li>
    </ul>

  <h2>Configuration</h2>
    <ul>
        <li>Python script uses PyQt5 for the graphical user interface.</li>
        <li>The script allows users to open a folder, select an image, apply filters, and save the edited image.</li>
    </ul>

  <h2>How to Run</h2>

  <ol>
        <li>Install Python 3.x on your machine.</li>
        <li>Install PyQt5 by running the following command in your terminal or command prompt:
            <pre>pip install PyQt5</pre>
        </li>
        <li>Save the provided Python script to a file with a <code>.py</code> extension.</li>
        <li>Run the script using the following command:
            <pre>python image.py</pre>
        
        </li>
  </ol>

  <p>Feel free to customize, extend, or modify this application according to your needs. Enjoy editing images!</p>

</body>

</html>
