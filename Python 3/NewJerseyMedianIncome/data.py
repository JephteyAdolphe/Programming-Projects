import pandas as pd
import numpy as np


class IncomeParser:

    def __init__(self, csvFile):
        self.colNames = ['Income Range', '# of People']
        df = pd.read_csv(csvFile, names=self.colNames, skip_blank_lines=True, usecols=[i for i in range(1, 3)])
        self.df = df.dropna()
        csvArr = np.array(self.df)
        self.csvArr = csvArr[10:]
        self.dataDict = {}
        self.medians = []
        self.countyKeys = []
        self.__parse()

    def __medianIncomePeople(self, individualsPer):
        individualsPer.sort()
        return individualsPer[3]

    def __parse(self):
        for i in range(189):
            incomesPerCounty = []

            if 'County' in self.csvArr[i][0]:
                counter = i
                self.countyKeys.append(self.csvArr[i][0])

                for people in range(counter + 2, counter + 9):
                    incomesPerCounty.append(int(self.csvArr[people][1]))

                self.medians.append(self.__medianIncomePeople(incomesPerCounty))

    def getCountyData(self):
        k = []
        for i in self.csvArr:
            for j in self.medians:
                if str(j) in i:
                    k.append(i[0])

        for i in range(len(self.countyKeys)):
            self.dataDict[self.countyKeys[i]] = k[i]

        return self.dataDict

    def getDataFrame(self):
        return self.df
