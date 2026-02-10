import textwrap
from PIL import Image, ImageDraw, ImageFont
import requests

class UniversalShare:
    def __init__(self):
        # Placeholder for your API Credentials
        self.credentials = {
            "x_api_key": "YOUR_X_KEY",
            "fb_access_token": "YOUR_FB_TOKEN",
            "ig_user_id": "YOUR_IG_ID"
        }

    def create_image_from_text(self, text, output_path="ig_post.png"):
        """Generates a 1080x1080 image if no image is provided."""
        img = Image.new('RGB', (1080, 1080), color=(30, 30, 30))
        canvas = ImageDraw.Draw(img)
        
        # Wrap text so it doesn't go off screen
        wrapper = textwrap.TextWrapper(width=20) 
        word_list = wrapper.wrap(text=text)
        caption = "\n".join(word_list)
        
        # Draw text in center (Using default font for compatibility)
        canvas.multiline_text((100, 400), caption, fill=(255, 255, 255), spacing=10)
        
        img.save(output_path)
        print(f"✅ Image generated: {output_path}")
        return output_path

    def summarize_for_x(self, text):
        """Limits text to 280 characters for X."""
        if len(text) <= 280:
            return text
        return text[:277] + "..."

    def post_to_x(self, text):
        content = self.summarize_for_x(text)
        print(f"🚀 Posting to X: {content}")
        # API call logic would go here

    def post_to_facebook(self, text, image_path=None):
        print(f"🚀 Posting to Facebook: {text[:30]}...")
        # API call logic would go here

    def run(self, user_input, image_provided=None):
        print("--- Processing Universal-Share ---")
        
        # 1. Handle X (Twitter)
        self.post_to_x(user_input)
        
        # 2. Handle Instagram/Facebook
        final_image = image_provided
        if not image_provided:
            final_image = self.create_image_from_text(user_input)
        
        self.post_to_facebook(user_input, final_image)
        print("--- All Posts Dispatched ---")

# --- EXECUTION ---
app = UniversalShare()

print("Welcome to Universal-Share")
my_post = input("Enter your post content: ")

# Run the automation
app.run(my_post)