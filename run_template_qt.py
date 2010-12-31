#!/usr/bin/env python3
# Copyright 2010 Hardcoded Software (http://www.hardcoded.net)
# 
# This software is licensed under the "BSD" License as described in the "LICENSE" file, 
# which should be included with this package. The terms are also available at 
# http://www.hardcoded.net/licenses/bsd_license

import sys
import sip
sip.setapi('QVariant', 1)

from PyQt4.QtCore import QCoreApplication
from PyQt4.QtGui import QApplication, QIcon, QPixmap

from qtlib.error_report_dialog import install_excepthook
from qt.base import dg_rc
from qt.{{edition}}.app import DupeGuru

if sys.platform == 'win32':
    import qt.base.cxfreeze_fix

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(QPixmap(":/{0}".format(DupeGuru.LOGO_NAME))))
    QCoreApplication.setOrganizationName('Hardcoded Software')
    QCoreApplication.setApplicationName(DupeGuru.NAME)
    QCoreApplication.setApplicationVersion(DupeGuru.VERSION)
    dgapp = DupeGuru()
    install_excepthook()
    sys.exit(app.exec_())