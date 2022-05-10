from rest_framework import views
import requests
from bs4 import BeautifulSoup
from .serializers import RankingSerializer
from rest_framework.response import Response


class RankingViewSet(views.APIView):

    def get(self, request):
        url = 'https://www.hltv.org/ranking/teams/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        r = requests.get(url, headers=headers)

        soup = BeautifulSoup(r.content, 'html.parser')
        ranking = soup.select('.name')
        images = soup.select('.team-logo img')

        newImages = []
        for image in images:
            try:
                if image['class'][0] == 'day-only':
                    newImages.append(image['src'])
            except:
                newImages.append(image['src'])


        rankingData = []
        for i, time in enumerate(ranking):
            rankingData.append({'position': i + 1,
                                'team': time.text,
                                'logo': newImages[i]})

        serializer = RankingSerializer(rankingData, many=True)

        return Response(serializer.data)