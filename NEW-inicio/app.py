from flask import Flask, Response, render_template, request, send_file, redirect, url_for, flash
import yt_dlp
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Ruta de descarga temporal para los videos
DOWNLOAD_FOLDER = 'downloads'
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/download', methods=['POST'])
def download_video():
    video_url = request.form.get('url')

    if not video_url:
        flash("Please enter a valid video URL.", "error")
        return redirect(url_for('index'))

    # Configuración para yt-dlp con soporte para Facebook
    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }]
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=True)
            filename = ydl.prepare_filename(info_dict)

        return send_file(
            filename,
            as_attachment=True,
            download_name=info_dict.get('title') + '.mp4',
            mimetype='video/mp4'
        )
    except Exception as e:
        flash(f"Error downloading video: {e}", "error")
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
