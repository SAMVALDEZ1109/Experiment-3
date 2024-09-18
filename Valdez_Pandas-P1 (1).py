{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "89aceb7e-9cc9-4948-840e-095fef977bf3",
   "metadata": {},
   "source": [
    "##EXPERIMENT 3 : Pyhton Data Analysis"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "91bc7107-329d-410d-b025-939e025697dd",
   "metadata": {},
   "source": [
    "#PROBLEM 1: \n",
    "\n",
    "Using knowledge obtained from the experiment and demonstrations:\r\n",
    "\r\n",
    "a. Load the corresponding .csv file into a data frame named cars using pandas\r\n",
    "\r\n",
    "b. Display the first five and last five rows of the resulting cars."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "5db5fdfc-36c2-4303-aee0-810363af79ca",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "First 5 rows: \n",
      "               Model   mpg  cyl   disp   hp  drat     wt   qsec  vs  am  gear  \\\n",
      "0          Mazda RX4  21.0    6  160.0  110  3.90  2.620  16.46   0   1     4   \n",
      "1      Mazda RX4 Wag  21.0    6  160.0  110  3.90  2.875  17.02   0   1     4   \n",
      "2         Datsun 710  22.8    4  108.0   93  3.85  2.320  18.61   1   1     4   \n",
      "3     Hornet 4 Drive  21.4    6  258.0  110  3.08  3.215  19.44   1   0     3   \n",
      "4  Hornet Sportabout  18.7    8  360.0  175  3.15  3.440  17.02   0   0     3   \n",
      "\n",
      "   carb  \n",
      "0     4  \n",
      "1     4  \n",
      "2     1  \n",
      "3     1  \n",
      "4     2  \n",
      "\n",
      "Last 6 rows: \n",
      "             Model   mpg  cyl   disp   hp  drat     wt  qsec  vs  am  gear  \\\n",
      "27    Lotus Europa  30.4    4   95.1  113  3.77  1.513  16.9   1   1     5   \n",
      "28  Ford Pantera L  15.8    8  351.0  264  4.22  3.170  14.5   0   1     5   \n",
      "29    Ferrari Dino  19.7    6  145.0  175  3.62  2.770  15.5   0   1     5   \n",
      "30   Maserati Bora  15.0    8  301.0  335  3.54  3.570  14.6   0   1     5   \n",
      "31      Volvo 142E  21.4    4  121.0  109  4.11  2.780  18.6   1   1     4   \n",
      "\n",
      "    carb  \n",
      "27     2  \n",
      "28     4  \n",
      "29     6  \n",
      "30     8  \n",
      "31     2  \n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Loading the CSV file into a dataframe named cars\n",
    "cars = \"http://bit.ly/Cars_file\"\n",
    "cars = pd.read_csv('cars.csv')\n",
    "\n",
    "# Displaying the first five and last five rows of the dataframe\n",
    "print(\"First 5 rows: \")\n",
    "print (cars.head())\n",
    "\n",
    "print(\"\\nLast 6 rows: \")\n",
    "print (cars.tail())"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
