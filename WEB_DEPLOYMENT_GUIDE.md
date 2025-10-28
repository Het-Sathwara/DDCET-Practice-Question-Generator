# Web Deployment Guide

Complete guide to deploy the DDCET Question Generator as a web application.

## Table of Contents
1. [Local Testing](#local-testing)
2. [Deploy to Render (Recommended)](#deploy-to-render)
3. [Deploy to Railway](#deploy-to-railway)
4. [Deploy to Vercel](#deploy-to-vercel)
5. [Deploy to Heroku](#deploy-to-heroku)
6. [Mobile Access](#mobile-access)

---

## Local Testing

### Run Locally

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Run the Flask app:**
```bash
python app.py
```

3. **Access in browser:**
```
http://localhost:5000
```

4. **Test on mobile (same network):**
   - Find your computer's IP address:
     ```bash
     # Linux/Mac
     ifconfig | grep "inet "
     
     # Windows
     ipconfig
     ```
   - Access from mobile: `http://YOUR_IP_ADDRESS:5000`

---

## Deploy to Render (Recommended - FREE)

Render offers free hosting with:
- Auto-deploy from GitHub
- HTTPS included
- Easy setup
- Mobile-friendly

### Steps:

1. **Push to GitHub** (already done):
   ```bash
   git add .
   git commit -m "Add web application"
   git push origin main
   ```

2. **Create Render Account:**
   - Go to https://render.com
   - Sign up with GitHub

3. **Create New Web Service:**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select `DDCET-Practice-Question-Generator`

4. **Configure Service:**
   - **Name:** `ddcet-question-generator`
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Instance Type:** `Free`

5. **Deploy:**
   - Click "Create Web Service"
   - Wait 2-3 minutes
   - Your app will be live at: `https://ddcet-question-generator.onrender.com`

6. **Access from Mobile:**
   - Open the URL on any device
   - Add to home screen for app-like experience!

---

## Deploy to Railway (FREE Alternative)

Railway is another excellent free option:

1. **Push to GitHub** (already done)

2. **Create Railway Account:**
   - Go to https://railway.app
   - Sign up with GitHub

3. **New Project:**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose `DDCET-Practice-Question-Generator`

4. **Configure:**
   - Railway auto-detects Python
   - It will use `Procfile` automatically
   - Click "Deploy"

5. **Get URL:**
   - Go to "Settings" → "Domains"
   - Click "Generate Domain"
   - Your app will be at: `https://your-app.railway.app`

---

## Deploy to Vercel (Serverless)

Good for quick deployments:

1. **Install Vercel CLI** (optional):
   ```bash
   npm install -g vercel
   ```

2. **Deploy from GitHub:**
   - Go to https://vercel.com
   - Sign up with GitHub
   - Import `DDCET-Practice-Question-Generator` repository
   - Click "Deploy"

3. **Your app will be live at:**
   ```
   https://ddcet-question-generator.vercel.app
   ```

Note: Vercel has limitations with long-running processes. Render or Railway is better for this app.

---

## Deploy to Heroku (Paid after free tier ends)

1. **Install Heroku CLI:**
   ```bash
   # Linux
   curl https://cli-assets.heroku.com/install.sh | sh
   
   # Mac
   brew tap heroku/brew && brew install heroku
   ```

2. **Login:**
   ```bash
   heroku login
   ```

3. **Create app:**
   ```bash
   heroku create ddcet-question-gen
   ```

4. **Deploy:**
   ```bash
   git push heroku main
   ```

5. **Open:**
   ```bash
   heroku open
   ```

---

## Mobile Access

### After Deployment:

1. **Open Browser on Mobile**
   - Navigate to your deployment URL
   - Example: `https://ddcet-question-generator.onrender.com`

2. **Add to Home Screen** (iOS):
   - Tap the Share button
   - Scroll down and tap "Add to Home Screen"
   - Name it "Question Generator"
   - Tap "Add"

3. **Add to Home Screen** (Android):
   - Tap the menu (⋮)
   - Select "Add to Home screen"
   - Name it "Question Generator"
   - Tap "Add"

4. **Now it works like an app!**
   - Full-screen experience
   - Fast access
   - All features available

### Features on Mobile:
- Generate questions
- Choose subjects & topics
- Select difficulty levels
- Preview questions
- Export to JSON/CSV/TXT
- View statistics
- Mobile-responsive design

---

## Troubleshooting

### Issue: App won't start
**Solution:**
- Check logs: `heroku logs --tail` (Heroku)
- Verify all dependencies in `requirements.txt`
- Ensure `Procfile` is correct

### Issue: Can't access from mobile
**Solution:**
- Check if URL is HTTPS (required for mobile)
- Clear browser cache
- Try different browser

### Issue: Export not working
**Solution:**
- Check browser settings allow downloads
- Try different format (JSON/CSV/TXT)
- Check mobile storage permissions

### Issue: Slow loading
**Solution:**
- Free tiers may take 30-60s to wake up
- Upgrade to paid plan for instant access
- Use Render/Railway for better free performance

---

## Features Comparison

| Feature | Render | Railway | Vercel | Heroku |
|---------|--------|---------|--------|--------|
| **Free Tier** | ✅ Yes | ✅ Yes | ✅ Yes | ⚠️ Limited |
| **HTTPS** | ✅ Auto | ✅ Auto | ✅ Auto | ✅ Auto |
| **Custom Domain** | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |
| **Sleep Time** | ~15 min | ~1 hour | None | ~30 min |
| **Build Time** | Fast | Fast | Very Fast | Medium |
| **Best For** | Full apps | Full apps | Static/API | Enterprise |

**Recommendation:** Use **Render** or **Railway** for this project (both have generous free tiers).

---

## Performance Tips

1. **Keep it awake** (free tiers sleep after inactivity):
   - Use a service like UptimeRobot to ping every 15 minutes
   - Or upgrade to paid tier ($7-10/month)

2. **Speed up loading:**
   - Use paid tier for instant access
   - Enable caching
   - Minimize session data

3. **Mobile optimization:**
   - Already included in the design
   - Works perfectly on all screen sizes
   - Touch-friendly buttons

---

## Security Notes

1. **Session Data:**
   - Stored temporarily in Flask sessions
   - Clears on browser close
   - No database required

2. **HTTPS:**
   - All platforms provide HTTPS automatically
   - Data is encrypted in transit

3. **Privacy:**
   - No user data collected
   - Questions generated on-the-fly
   - Export files stored locally on user's device

---

## Support

If you have issues deploying:

1. **Check the logs** on your hosting platform
2. **Verify** all files are pushed to GitHub
3. **Test locally** first with `python app.py`
4. **Contact** the hosting platform's support

---

## Next Steps

After deployment:

1. ✅ Share the URL with students
2. ✅ Add to mobile home screens
3. ✅ Create mock tests
4. ✅ Generate practice questions
5. ✅ Export and share question sets

**Your web app is production-ready!** 🎉

---

**Last Updated:** October 2025  
**Platform:** Flask + Python  
**License:** Educational Use

