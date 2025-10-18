# 🎭 $FORK - Random Meme Display

A dynamic, immersive website showcasing your collection of 141 memes with random positioning and timing. Features the $FORK token prominently displayed in the center.

## 🚀 Features

- **Random Positioning**: Memes appear in random locations across the screen
- **Dynamic Timing**: New memes appear every 3 seconds, stay for 20 seconds
- **Random Sizing**: Each meme displays in a random size (small, medium, large, or extra-large)
- **Token Display**: $FORK token and contract address prominently centered
- **Fullscreen View**: Click any meme to view it in fullscreen
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile
- **Beautiful Animations**: Smooth fade-in/fade-out effects with rotation
- **Dynamic Background**: Background color shifts every 20 seconds
- **Floating Particles**: Subtle particle effects for ambiance

## 🎨 Design Features

- **Centered Token Info**: $FORK symbol and contract address in the center
- **Random Meme Placement**: Memes avoid the center area to keep token info visible
- **Smooth Animations**: Memes fade in with scale and rotation effects
- **Gradient Backgrounds**: Dynamic color-shifting backgrounds
- **Hover Effects**: Memes scale up slightly on hover
- **No Grid Layout**: Completely free-form positioning

## 📁 File Structure

```
flork/
├── index.html          # Main HTML file
├── styles.css          # CSS styling and animations
├── script.js           # JavaScript functionality
├── memes/              # Your meme collection (141 images)
└── README.md           # This file
```

## 🌐 How to View

1. **Local Server** (Recommended):
   ```bash
   python3 -m http.server 8000
   ```
   Then open: http://localhost:8000

2. **Direct File**: Simply open `index.html` in your browser

## 🎯 How It Works

- **Automatic Display**: Memes appear automatically every 3 seconds
- **Random Locations**: Each meme appears in a random position (avoiding center)
- **20-Second Lifetime**: Each meme stays visible for exactly 20 seconds
- **Maximum 8 Memes**: Up to 8 memes can be on screen simultaneously
- **Click to View**: Click any meme for fullscreen viewing
- **Responsive**: Automatically adjusts to different screen sizes

## 🎨 Token Information

The website prominently displays:
- **$FORK** - Large, glowing token symbol
- **Contract Address**: CA: 4dECjiqwxeGrX7eGgYbMNRg5ib5RkjFA2kbTsDdYpump

## 📱 Mobile Friendly

The website automatically adapts to different screen sizes:
- **Desktop**: Full-size memes with large token display
- **Tablet**: Medium-sized memes with adjusted token size
- **Mobile**: Smaller memes with compact token display

## 🎨 Customization

The website is built with modern web technologies and is easily customizable:

- **Timing**: Adjust meme appearance interval and lifetime in `script.js`
- **Colors**: Edit the gradient colors in `styles.css`
- **Animations**: Modify animation durations and effects
- **Token Info**: Update token symbol and address in `index.html`
- **Meme Limits**: Change maximum concurrent memes in `script.js`

Enjoy your dynamic meme display! 🎉
