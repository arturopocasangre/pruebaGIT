from flask import Flask, render_template, request, redirect, url_for
from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()


print("URL:", os.getenv("SUPABASE_URL"))
print("KEY:", os.getenv("SUPABASE_KEY")[:10] + "...")

app = Flask(__name__)

# Conexión a Supabase
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

@app.route('/')
def index():
    data = supabase.table("productos").select("*").execute()
    productos = data.data
    return render_template("index.html", productos=productos)

@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = float(request.form['precio'])
        stock = int(request.form['stock'])
        supabase.table("productos").insert({
            "nombre": nombre,
            "descripcion": descripcion,
            "precio": precio,
            "stock": stock
        }).execute()
        return redirect(url_for('index'))
    return render_template("agregar.html")

@app.route('/eliminar/<int:id>')
def eliminar(id):
    supabase.table("productos").delete().eq("id", id).execute()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
