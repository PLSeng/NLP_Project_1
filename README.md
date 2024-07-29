# NLP Project 1

## Status
[![Makefile CI](https://github.com/PLSeng/NLP_Project_1/actions/workflows/makefile.yml/badge.svg)](https://github.com/PLSeng/NLP_Project_1/actions/workflows/makefile.yml)

## Introduction
This project is about the implementation of a simple text classification system and command line interface for it. This is a wikipedia summary and get the noun phrases in the summary. The system use the Wikipedia API to get the summary of a given topic and then use the TextBlob library to extract the noun phrases from the summary. The system then uses a simple text classification model to classify the noun phrases into one of the following categories: person, organization, location, or other. The system then prints the classified noun phrases along with the category they belong to.

## Requirements
- Python 3.6 or higher
- TextBlob
- Wikipedia-API

## Installation
```bash
make install
```