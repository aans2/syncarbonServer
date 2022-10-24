from django.shortcuts import render
from django.core.files.base import ContentFile
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import parser_classes
from rest_framework.parsers import FileUploadParser
from django.core import serializers

from combustivel.models import Bomba, Combustivel


from PyPDF2 import PdfReader
import json, datetime, base64, os

class CombustivelConsumo(APIView):

    def get(self, request):
        comb = Combustivel.objects.all()

        data = serializers.serialize("json", comb)

        print("data", data)

        return Response(data)

    def post(self, request):

        a = os.listdir('./relatorio')

        if json.loads(request.body)['mes'] == 1:
            reader = PdfReader("./relatorio/JAN.pdf")
        if json.loads(request.body)['mes'] == 2:
            reader = PdfReader("./relatorio/FEV.pdf")
        if json.loads(request.body)['mes'] == 3:
            reader = PdfReader("./relatorio/MAR.pdf")
        if json.loads(request.body)['mes'] == 4:
            reader = PdfReader("./relatorio/ABR.pdf")
        if json.loads(request.body)['mes'] == 5:
            reader = PdfReader("./relatorio/MAI.pdf")
        if json.loads(request.body)['mes'] == 6:
            reader = PdfReader("./relatorio/JUN.pdf")
        if json.loads(request.body)['mes'] == 7:
            reader = PdfReader("./relatorio/JUL.pdf")
        if json.loads(request.body)['mes'] == 8:
            reader = PdfReader("./relatorio/AGO.pdf")
        if json.loads(request.body)['mes'] == 9:
            reader = PdfReader("./relatorio/SET.pdf")
        if json.loads(request.body)['mes'] == 10:
            reader = PdfReader("./relatorio/OUT.pdf")
        if json.loads(request.body)['mes'] == 11:
            reader = PdfReader("./relatorio/NOV.pdf")
        if json.loads(request.body)['mes'] == 12:
            reader = PdfReader("./relatorio/DEZ.pdf")

        page = reader.pages[0]
        parts = []

        def visitor_body(text, cm, tm, fontDict, fontSize):
            y = tm[5]
            if y > 500 and y < 720:
                parts.append(text.strip())

        page.extract_text(visitor_text=visitor_body)
        text_body = "".join(parts)

        parts = list(filter(('').__ne__, parts))

        pos = [parts[1],parts[5],parts[9],parts[13],parts[17],parts[21]]
        val = [parts[3],parts[7],parts[11],parts[15],parts[19],parts[23]]

        for x in range(6):
            bom = Bomba.objects.get(name=pos[x])
            print("bom", bom)
            comb = Combustivel(
                bomba = bom,
                valor = val[x]
            )
            comb.save()

        return Response()