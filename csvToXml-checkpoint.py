{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "48b3003e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# convert csv to xml"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "6e79f990",
   "metadata": {},
   "outputs": [],
   "source": [
    "#glonal import\n",
    "import pandas as pd\n",
    "import time\n",
    "import os\n",
    "import sys"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "6a57cef2",
   "metadata": {},
   "outputs": [],
   "source": [
    "csvPath = \"https://people.sc.fsu.edu/~jburkardt/data/csv/addresses.csv\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "0ef8ada7",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv(csvPath)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "43f2d6ea",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Function to convert csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "3a940fd2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>John</th>\n",
       "      <th>Doe</th>\n",
       "      <th>120 jefferson st.</th>\n",
       "      <th>Riverside</th>\n",
       "      <th>NJ</th>\n",
       "      <th>08075</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Jack</td>\n",
       "      <td>McGinnis</td>\n",
       "      <td>220 hobo Av.</td>\n",
       "      <td>Phila</td>\n",
       "      <td>PA</td>\n",
       "      <td>9119</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>John \"Da Man\"</td>\n",
       "      <td>Repici</td>\n",
       "      <td>120 Jefferson St.</td>\n",
       "      <td>Riverside</td>\n",
       "      <td>NJ</td>\n",
       "      <td>8075</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Stephen</td>\n",
       "      <td>Tyler</td>\n",
       "      <td>7452 Terrace \"At the Plaza\" road</td>\n",
       "      <td>SomeTown</td>\n",
       "      <td>SD</td>\n",
       "      <td>91234</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>NaN</td>\n",
       "      <td>Blankman</td>\n",
       "      <td>NaN</td>\n",
       "      <td>SomeTown</td>\n",
       "      <td>SD</td>\n",
       "      <td>298</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Joan \"the bone\", Anne</td>\n",
       "      <td>Jet</td>\n",
       "      <td>9th, at Terrace plc</td>\n",
       "      <td>Desert City</td>\n",
       "      <td>CO</td>\n",
       "      <td>123</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                    John       Doe                 120 jefferson st.  \\\n",
       "0                   Jack  McGinnis                      220 hobo Av.   \n",
       "1          John \"Da Man\"    Repici                 120 Jefferson St.   \n",
       "2                Stephen     Tyler  7452 Terrace \"At the Plaza\" road   \n",
       "3                    NaN  Blankman                               NaN   \n",
       "4  Joan \"the bone\", Anne       Jet               9th, at Terrace plc   \n",
       "\n",
       "     Riverside   NJ   08075  \n",
       "0        Phila   PA    9119  \n",
       "1    Riverside   NJ    8075  \n",
       "2     SomeTown   SD   91234  \n",
       "3     SomeTown   SD     298  \n",
       "4  Desert City   CO     123  "
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "510ce486",
   "metadata": {},
   "outputs": [],
   "source": [
    "def xmlWriter(row):\n",
    "    return \"\"\"<Joe=\"%s\">\n",
    "    <Doe>%s</type>\n",
    "    <Riverside>%s</year>\n",
    "</Joe>\"\"\" % (\n",
    "    row.John, row.Doe, row.Riverside)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "5b7eb30f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<Joe=\"Jack\">\n",
      "    <Doe>McGinnis</type>\n",
      "    <Riverside>Phila</year>\n",
      "</Joe>\n",
      "<Joe=\"John \"Da Man\"\">\n",
      "    <Doe>Repici</type>\n",
      "    <Riverside>Riverside</year>\n",
      "</Joe>\n",
      "<Joe=\"Stephen\">\n",
      "    <Doe>Tyler</type>\n",
      "    <Riverside>SomeTown</year>\n",
      "</Joe>\n",
      "<Joe=\"nan\">\n",
      "    <Doe>Blankman</type>\n",
      "    <Riverside>SomeTown</year>\n",
      "</Joe>\n",
      "<Joe=\"Joan \"the bone\", Anne\">\n",
      "    <Doe>Jet</type>\n",
      "    <Riverside>Desert City</year>\n",
      "</Joe>\n"
     ]
    }
   ],
   "source": [
    "print ('\\n'.join(df.apply(xmlWriter, axis=1)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eb192921",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
