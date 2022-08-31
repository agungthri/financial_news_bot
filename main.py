import bot_engine
import asyncio

if __name__ == "__main__":

    try:
        isRun = input("Jalankan Bot News ? [y/n] : ")
        if isRun == 'Y' or 'y':
            print('Tekan CTRL + C Untuk Keluar')
            asyncio.run(bot_engine.main())
        else:
            print('Perintah Tidak Dijalankan')
    except KeyboardInterrupt:
        print("keluar Dari Program")
