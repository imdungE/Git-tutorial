{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOCSarEJskBVYxZbXlgAQWq",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/imdungE/Git-tutorial/blob/main/Untitled0.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DQJ5DxHGa4V3",
        "outputId": "05d7e847-f90c-4e7f-d0b6-25e883bc5078"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[100, 92, 90, 73, 34, 100, 25]\n",
            "[44, 0, 67, 98, 75, 99, 95]\n",
            "['김수뭉', '이상명', '박자하']\n",
            "['최월해', '문드림', '조미래']\n",
            "['김수뭉', '이상명', '박자하', '최월해', '문드림']\n",
            "조미래 사망\n"
          ]
        }
      ],
      "source": [
        "score_math = [92, 90, 73, 34, 100]\n",
        "score_eng = [44, 67, 98, 75, 99]\n",
        "\n",
        "score_math.append(25)\n",
        "score_eng.append(95)\n",
        "\n",
        "score_math.insert(0, 100)\n",
        "score_eng.insert(1, 0)\n",
        "\n",
        "print(score_math)\n",
        "print(score_eng)\n",
        "\n",
        "waiting_am = ['김수뭉', '이상명', '박자하']\n",
        "waiting_pm = ['최월해', '문드림', '조미래']\n",
        "waiting_total = waiting_am + waiting_pm\n",
        "\n",
        "kill = waiting_total.pop()\n",
        "\n",
        "print(waiting_am)\n",
        "print(waiting_pm)\n",
        "print(waiting_total)\n",
        "print(kill + \" 사망\")"
      ]
    }
  ]
}