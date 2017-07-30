#
# Copyright (c) 2017 nexB Inc. and others. All rights reserved.
# http://nexb.com and https://github.com/nexB/scancode-server/
# The scancode-server software is licensed under the Apache License version 2.0.
# Data generated with scancode-server require an acknowledgment.
#
# You may not use this software except in compliance with the License.
# You may obtain a copy of the License at: http://apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
#
# When you publish or redistribute any data created with scancode-server or any scancode-server
# derivative work, you must accompany this data with the following acknowledgment:
#
#  Generated with scancode-server and provided on an "AS IS" BASIS, WITHOUT WARRANTIES
#  OR CONDITIONS OF ANY KIND, either express or implied. No content created from
#  scancode-server should be considered or used as legal advice. Consult an Attorney
#  for any legal advice.
#  scancode-server is a free software code scanning tool from nexB Inc. and others.
#  Visit https://github.com/nexB/scancode-server/ for support and download.

from django.test import TestCase
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files import File

from scanapp.forms import UrlScanForm
from scanapp.forms import LocalScanForm

class UrlScanFormTestCase(TestCase):
    def test_correct_url_scan_form(self):
        correct_form_data = {'url': 'https://github.com'}
        correct_url_scan_form = UrlScanForm(data=correct_form_data)
        self.assertTrue(correct_url_scan_form.is_valid())
        self.assertEqual('https://github.com', correct_url_scan_form.data['url'])
    
    def test_wrong_url_scan_form(self):
        wrong_form_data = {'url': 'not an URL'}
        wrong_url_scan_form = UrlScanForm(data=wrong_form_data)
        self.assertFalse(wrong_url_scan_form.is_valid())    
    
    def test_empty_url_scan_form(self):
        empty_form_data = {'url': ''}
        empty_url_scan_form = UrlScanForm(data=empty_form_data)
        self.assertFalse(empty_url_scan_form.is_valid())

#class LocalScanFormTestCase(TestCase):
#    def test_local_scan_form(self):
#        a_file = InMemoryUploadedFile('name', 'local', 'name.txt', 400, 'application/json', 'utf-8', 'no extra')
#        correct_form_data = {'upload_from_local': a_file}
#        wrong_form_data = {'upload_from_local': 'not a path'}
#        empty_form_data = {'upload_from_local': ''}
#        correct_local_scan_form = LocalScanForm(data=correct_form_data)
#        wrong_local_scan_form = LocalScanForm(data=wrong_form_data)
#        empty_local_scan_form = LocalScanForm(data=empty_form_data)
#        self.assertEqual('name.txt', str(a_file))
#        self.assertTrue(correct_local_scan_form.is_valid())
#        self.assertEqual('/home/ranvir/Documents/file.txt', correct_local_scan_form.data['upload_from_local'])
#        self.assertFalse(wrong_local_scan_form.is_valid())
#        self.assertFalse(empty_local_scan_form.is_valid())