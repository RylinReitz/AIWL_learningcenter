// Minimal API client used by static pages when served via backend
async function apiGet(path){
    const res = await fetch('/api' + path);
    return res.json();
}
