# Deploy to Render.com - Step by Step Guide

## Why Render for Flask Apps?
- ✅ FREE tier (forever)
- ✅ Perfect for Flask/Python apps
- ✅ Auto-deploy from GitHub
- ✅ HTTPS included
- ✅ Works on mobile
- ✅ No credit card required

## Deployment Steps (3 Minutes)

### Step 1: Sign Up on Render

1. Go to **https://render.com**
2. Click **"Get Started"**
3. Sign up with your GitHub account
4. Authorize Render to access your repositories

### Step 2: Create New Web Service

1. Click **"New +"** button (top right)
2. Select **"Web Service"**

### Step 3: Connect Repository

1. You'll see a list of your GitHub repositories
2. Find **"DDCET-Practice-Question-Generator"**
3. Click **"Connect"**

### Step 4: Configure Service

Fill in these settings:

**Basic Settings:**
- **Name:** `ddcet-question-generator` (or any name you want)
- **Region:** Select closest to you (e.g., Singapore, Oregon)
- **Branch:** `main`
- **Root Directory:** Leave blank
- **Runtime:** `Python 3`

**Build Settings:**
- **Build Command:** 
  ```
  pip install -r requirements.txt
  ```

- **Start Command:**
  ```
  gunicorn app:app
  ```

**Instance Type:**
- Select **"Free"** (not the paid one!)

### Step 5: Deploy

1. Click **"Create Web Service"**
2. Render will start building your app
3. You'll see a live log of the deployment
4. Wait 2-3 minutes for first deployment

### Step 6: Get Your URL

1. Once deployed, you'll see: **"Your service is live 🎉"**
2. Your URL will be something like:
   ```
   https://ddcet-question-generator.onrender.com
   ```
3. Click the URL to open your app!

## Access from Mobile

1. Open the URL on your phone: `https://your-app-name.onrender.com`
2. **Add to Home Screen:**
   - **iPhone:** Tap Share → "Add to Home Screen"
   - **Android:** Tap Menu (⋮) → "Add to home screen"
3. Now it works like a native app!

## Important Notes

### Free Tier Limitations:
- App sleeps after 15 minutes of inactivity
- First request after sleep takes ~30 seconds to wake up
- After that, it's fast!
- Perfect for practice/testing

### Keep It Awake (Optional):
If you want instant access, use a free service like:
- **UptimeRobot** (https://uptimerobot.com)
- Ping your URL every 14 minutes
- Prevents sleeping

### Upgrade (Optional):
- $7/month for always-on service
- No sleep time
- Faster response

## Troubleshooting

### Build Failed?
- Check the logs in Render dashboard
- Verify `requirements.txt` is correct
- Make sure all files are pushed to GitHub

### App Not Loading?
- Wait 30 seconds (it might be waking up)
- Check Render logs for errors
- Verify the Start Command is: `gunicorn app:app`

### Can't Access from Mobile?
- Make sure you're using the HTTPS URL
- Clear browser cache
- Try a different browser

## Auto-Deploy

Render automatically deploys when you push to GitHub:

```bash
# Make changes to your code
git add .
git commit -m "Update feature"
git push origin main

# Render automatically detects and deploys!
```

## Custom Domain (Optional)

1. Go to your service settings on Render
2. Click "Custom Domain"
3. Add your domain (e.g., questions.yourdomain.com)
4. Follow DNS instructions
5. FREE HTTPS certificate included!

## Environment Variables (If Needed)

If you need to add secrets or config:

1. Go to "Environment" tab
2. Add key-value pairs
3. Click "Save Changes"
4. App will auto-redeploy

## Monitoring

Render provides:
- Real-time logs
- Metrics (CPU, Memory)
- Deploy history
- Automatic health checks

## Support

If you have issues:
- Check Render's documentation: https://render.com/docs
- Visit their community forum
- Email support: support@render.com

---

**Your app is now live and accessible from anywhere! 🚀**

