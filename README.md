# GeoJSON Uploader

## Türkçe Açıklama

Bu uygulama, GeoJSON formatındaki dosyaları PostgreSQL veritabanına yüklemek için kullanılabilir. Uygulama, veritabanı bağlantı bilgilerini girdikten sonra bir GeoJSON dosyasını seçmenizi sağlar ve ardından bu veriyi PostgreSQL veritabanında belirtilen bir tabloya kaydeder.
![main page](https://github.com/user-attachments/assets/617352aa-d1f7-46ee-b608-10defff7f70f)
![1](https://github.com/user-attachments/assets/8f254d95-03f7-49cd-9304-2ac5dd9b51de)
![2](https://github.com/user-attachments/assets/d693b0cd-4c2f-4487-86f1-feb7571cef6e)

### Özellikler:
- PostgreSQL veritabanına bağlanarak GeoJSON dosyasını yükler.
- Kullanıcı dostu grafiksel arayüz.
- Bağlantı testi ve dosya seçimi özellikleri.
- Uygulama başarıyla çalıştığında veritabanında yeni bir tablo oluşturulur.

### Kullanım:
1. Uygulamayı çalıştırın.
2. Veritabanı bağlantı bilgilerini girin (host, port, kullanıcı adı, şifre, veritabanı adı).
3. "Test Connection" butonuna tıklayın. Bağlantı başarılı ise, bir dosya seçme kutusu ve tablo adı girebileceğiniz alan açılacaktır.
4. GeoJSON dosyasını seçin ve veritabanında oluşturulacak tablonun adını yazın.
5. "Save" butonuna tıklayarak dosyayı veritabanına yükleyin.

### Gereksinimler:
- Python 3.x
- tkinter (GUI için)
- psycopg2 (PostgreSQL bağlantısı için)
- osgeo (ogr2ogr komutunu çalıştırmak için)

### Kurulum:
1. Python 3.x yüklü olduğundan emin olun.
2. Aşağıdaki komutla gerekli kütüphaneleri yükleyin:
    ```bash
    pip install tkinter psycopg2 osgeo
    ```

3. Uygulamanızı çalıştırın:
    ```bash
    python app.py
    ```

---

## English Description

This application allows you to upload GeoJSON files to a PostgreSQL database. After entering the database connection details, it enables you to select a GeoJSON file and then saves the data into a specified table in the PostgreSQL database.

### Features:
- Connects to a PostgreSQL database and uploads a GeoJSON file.
- User-friendly graphical interface.
- Connection testing and file selection options.
- A new table is created in the database once the operation is successful.

### Usage:
1. Run the application.
2. Enter the database connection details (host, port, username, password, database name).
3. Click the "Test Connection" button. If the connection is successful, a file selection dialog and a field to enter the table name will appear.
4. Choose the GeoJSON file and enter the name for the table to be created in the database.
5. Click "Save" to upload the data to the database.

### Requirements:
- Python 3.x
- tkinter (for GUI)
- psycopg2 (for PostgreSQL connection)
- osgeo (to execute the ogr2ogr command)

### Installation:
1. Make sure Python 3.x is installed.
2. Install the necessary libraries by running:
    ```bash
    pip install tkinter psycopg2 osgeo
    ```

3. Run your application:
    ```bash
    python app.py
    ```
