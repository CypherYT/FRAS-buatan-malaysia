echo "installing python3"
sudo apt-get install python3
sudo apt-get install pip-python3
echo "MAKE SURE YOU HAVE ENOUGH SWAPFILE(minimum 8GB) IN ORDER TO BUILD face_recognition!"
echo "do-you-wish-to-proceed? type yes or no without capital"
read varyesno
if [ $varyesno="yes"]
then
  echo "installing dependencies"
  pip install cmake
  pip install face_recognition
  pip install colorama
  pip install numpy
  pip install cv2
  python3 -m pip
  echo "[OK] PROGRAM IS INSTALLED"
else
  echo "aborting" 
fi

