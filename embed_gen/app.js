function generateCommand() {
    const title = document.getElementById('title').value;
    let description = document.getElementById('description').value;
    const header = document.getElementById('header').value;
    const footer = document.getElementById('footer').value;
    const icon = document.getElementById('icon').value;
    const image = document.getElementById('image').value;
  
    // Replace new lines with \n escape sequence
    description = description.replace(/\n/g, '\\n');
  
    let command = `!embed ${title} (${description})`;
  
    if (header !== '') {
      command += ` [header=${header}]`;
    }
  
    if (footer !== '') {
      command += ` [footer=${footer}]`;
    }
   
    if (icon !== '') {
      command += ` [icon=${icon}]`;
    }

    if (image !== '') {
      command += ` [image=${image}]`;
    }
  
    document.getElementById('result').innerHTML = command;
  }

function copyCommand() {
  const commandText = document.getElementById('result').innerText;
  navigator.clipboard.writeText(commandText);
}