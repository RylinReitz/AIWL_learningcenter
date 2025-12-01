document.getElementById('run').addEventListener('click', async () => {
  const prompt = document.getElementById('prompt').value;
  const out = document.getElementById('out');
  out.textContent = 'Running...';
  try {
    const res = await fetch('/api/prompts/run', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({prompt, max_tokens: 256})
    });
    const data = await res.json();
    out.textContent = data.response;
  } catch (e) {
    out.textContent = 'Error: ' + e.toString();
  }
});
